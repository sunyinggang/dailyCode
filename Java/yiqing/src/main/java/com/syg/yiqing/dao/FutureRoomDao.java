package com.syg.yiqing.dao;

import com.syg.yiqing.entity.FutureRoom;
import com.syg.yiqing.entity.TraditionalOffice;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface FutureRoomDao extends JpaRepository<FutureRoom, Integer> {

    @Override
    Page<FutureRoom> findAll(Pageable pageable);

    Page<FutureRoom> findAllByCity(Pageable pageable,String city);
}
