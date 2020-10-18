package com.syg.yiqing.dao;

import com.syg.yiqing.entity.SignBuilding;
import org.springframework.data.domain.Example;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface SignBuildingDao extends JpaRepository<SignBuilding, Integer>{

    @Override
    Page<SignBuilding> findAll(Pageable pageable);
}
