package com.syg.yiqing.dao;

import com.syg.yiqing.entity.FutureRoom;
import com.syg.yiqing.entity.Property;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PropertyDao extends JpaRepository<Property, Integer> {

    @Override
    Page<Property> findAll(Pageable pageable);

}
